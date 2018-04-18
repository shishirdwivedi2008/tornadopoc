import tornado.ioloop;
import tornado.web
from datetime import date
from SomeData import SomeData

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response={"version":"1.0.0","time":date.today().isoformat() }
        self.write(response)


application=tornado.web.Application([

    (r"/version",VersionHandler),(r"/SomeData",SomeData)
])

if __name__=="__main__":
    application.listen(8888)
    print("Listnening on port 8888")
    tornado.ioloop.IOLoop.instance().start()