from objc_util import ObjCClass
import ui

import pdbg

#GLKView = ObjCClass('GLKView').alloc()
#pdbg.state(GLKView)



class ViewController(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'slategra'
    self.viewDidLoad()
    
  def viewDidLoad(self):
    f = ((0.0, 0.0), (100.0, 100.0))
    self.glview = ObjCClass('GLKView').alloc()
    self.glview.initWithFrame_(f)
    self.glview.setAutoresizingMask_((1 << 1) | (1 << 4))
    
    self.glview.context = ObjCClass('EAGLContext').alloc().initWithAPI_(2)  # kEAGLRenderingAPIOpenGLES2
    self.objc_instance.addSubview_(self.glview)
    EAGLContext = ObjCClass('EAGLContext')
    EAGLContext.setCurrentContext_(self.glview.context())
    self.baseEffect = ObjCClass('GLKBaseEffect').alloc().init()
    pdbg.state(baseEffect)
    
    
    
    




if __name__ == '__main__':
  vc = ViewController()
  vc.present(style='fullscreen', orientations=['portrait'])
