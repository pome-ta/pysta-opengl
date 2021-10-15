from objc_util import ObjCClass
import ui

import pdbg


class ViewController(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'slategra'
    self.viewDidLoad()

  def viewDidLoad(self):
    self.setupGL()

  def setupGL(self):
    EAGLContext = ObjCClass('EAGLContext').alloc()
    context = EAGLContext.initWithAPI_(3)
    pdbg.state(context.API())


if __name__ == '__main__':
  vc = ViewController()
  vc.present(style='fullscreen', orientations=['portrait'])

