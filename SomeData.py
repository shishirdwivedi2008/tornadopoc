from datetime import date

import tornado.web
import tornado.ioloop


class SomeData(tornado.web.RequestHandler):
    def get(self):
        response={"value":"This is some data response"}
        self.write(response)
