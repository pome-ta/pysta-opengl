from objc_util import ObjCClass
import ui

import pdbg



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

    # todo: OpenGL ES 2を使う
    #EAGLContext = ObjCClass('EAGLContext')
    #self.glview.context = EAGLContext.alloc().initWithAPI_(2)  # kEAGLRenderingAPIOpenGLES2
    self.glview.context = ObjCClass('EAGLContext').alloc().initWithAPI_(2)  # kEAGLRenderingAPIOpenGLES2
    self.objc_instance.addSubview_(self.glview)

    # xxx: delegate `self.glview.delegate = self;`

    # todo: 生成したコンテキストをカレントコンテキストに設定
    ObjCClass('EAGLContext').setCurrentContext_(self.glview.context())
    self.baseEffect = ObjCClass('GLKBaseEffect').alloc().init()
    self.baseEffect.useConstantColor = 1  # GL_TRUE
    
    
    pdbg.state(self.baseEffect.constantColor())


if __name__ == '__main__':
  vc = ViewController()
  vc.present(style='fullscreen', orientations=['portrait'])

