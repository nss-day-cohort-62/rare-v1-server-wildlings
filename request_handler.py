from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
from views import (
    get_all_posts,
    get_single_post,
    get_all_categories,
    create_category,
    get_all_tags,
    create_tag,
    create_post,
    delete_post,
    update_post
)
from views.user import create_user, login_user


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header(
            'Access-Control-Allow-Methods',
            'GET, POST, PUT, DELETE'
        )
        self.send_header(
            'Access-Control-Allow-Headers',
            'X-Requested-With, Content-Type, Accept'
        )
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        (resource, id, query_params) = parsed

        if resource == "posts":
            if id is not None:
                response = get_single_post(id)

            else:
                response = get_all_posts(query_params)
        if resource == "categories":
            if id is not None:
                pass

            else:
                response = get_all_categories()
        if resource == "tags":
            if id is not None:
                pass

            else:
                response = get_all_tags()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, _, _) = self.parse_url(self.path)

        new_category = None
        new_tag = None
        new_post = None
        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            new_category = create_category(post_body)
            self.wfile.write(json.dumps(new_category).encode())
        if resource == 'tags':
            new_tag = create_tag(post_body)
            self.wfile.write(json.dumps(new_tag).encode())
        if resource == 'posts':
            new_post = create_post(post_body)
            self.wfile.write(json.dumps(new_post).encode())

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id, _) = self.parse_url(self.path)

        success = False

        # Update a single animal in the list
        if resource == "posts":
            success = update_post(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)

        # Parse the URL
        (resource, id, _) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "posts":
            delete_post(id)

        # Encode the new animal and send in a response
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
