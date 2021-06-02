import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
import test as t


PORT = 8080

genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"}

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)
        human_g_list = []
        for key, ID in genes_dict.items():
            gene = key
            human_g_list.append(gene)
        context = {}
        if path_name == "/":
            context = {"human_genes": human_g_list}
            contents = su.read_template_html_file("HTML/INDEX.html").render(context=context)
        elif path_name == "/listSpecies":
            try:
                limit_number = arguments["limit"][0]
                if 0 <= int(limit_number) <= 310:
                    contents = t.species_name(int(limit_number))
                elif int(limit_number) >= 310:
                    contents = t.species_name(310)
                else:
                    contents = su.read_template_html_file("./HTML/ERROR.html").render()
            except ValueError:
                contents = su.read_template_html_file("./HTML/ERROR.html").render()

            #try:
                #try:
                    #try:
                        #limit_number = arguments["limit"][0]
                        #contents = t.species_name(int(limit_number))
                    #except KeyError:
                        #contents = su.read_template_html_file("./HTML/ERROR.html").render()
                #except ValueError:
                    #contents = su.read_template_html_file("./HTML/ERROR.html").render()
            #except IndexError:
                #contents = su.read_template_html_file("./HTML/ERROR.html").render()
        elif path_name == "/karyotype":
            try:
                specie = arguments["karyotype"][0]
                contents = t.karyotype(specie)
                print(type(specie))
            except KeyError:
                contents = su.read_template_html_file("./HTML/ERROR.html").render()
        elif path_name == "/chromosomeLength":
            try:
                try:
                    specie = arguments["specie"][0]
                    number = arguments["number"][0]
                    contents = t.chromosmes(specie,number)
                except KeyError:
                    contents = su.read_template_html_file("./HTML/ERROR.html").render()
            except UnboundLocalError:
                contents = su.read_template_html_file("./HTML/ERROR.html").render()
        elif path_name == "/geneSeq":
            gene = arguments["gene"][0]
            contents = t.geneSeq(gene, genes_dict)
        elif path_name == "/geneInfo":
            gene = arguments["gene"][0]
            contents = t.infoSeq(gene, genes_dict)
        elif path_name == "/geneCalc":
            gene = arguments["gene"][0]
            type_info = arguments["calculation"][0]
            if type_info == "length":
                contents = t.lengthSeq(gene, genes_dict)
            elif type_info == "percentage":
                contents = t.percentageSeq(gene, genes_dict)











        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/HTML')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("IT IS STOP BY THE USER")
        httpd.server_close()