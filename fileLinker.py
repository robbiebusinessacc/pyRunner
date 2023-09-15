from AppKit import NSApplication, NSStatusBar, NSStatusItem, NSVariableStatusItemLength, NSMenu, NSMenuItem, NSTimer
import glob, sys

class MacOSMenuBar(object):

    def __init__(self):
        self.statusbar = NSStatusBar.systemStatusBar()
        self.statusitem = self.statusbar.statusItemWithLength_(NSVariableStatusItemLength)
        self.statusitem.setTitle_('File Runner')
        self.statusitem.setHighlightMode_(True)
        self.statusitem.setToolTip_('MacOS Menu Bar')

        # create menu for the statusitem
        self.menu = NSMenu.alloc().init()
        self.statusitem.setMenu_(self.menu)
        
        self.fileLinker()

    def fileLinker(self):
        sys.path.insert(0, './new')

        # creates a list of files in the 'new' directory
        files = [file.replace('new/', '') for file in glob.glob("new/*.py") if file != 'fileLinker.py']

        for file in files:
            menuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(file, "runPythonFile:", "")
            menuItem.setRepresentedObject_(file)  # store filename in the menuItem
            menuItem.setTarget_(self)
            self.menu.addItem_(menuItem)

    def runPythonFile_(self, sender):
        file = sender.representedObject()
        file_path = f'./new/{file}'
        namespace = {'__file__': file_path, '__name__': '__main__'}
        
        try:
            with open(file_path, 'r') as f:
                code = compile(f.read(), file, 'exec')
                exec(code, namespace, namespace)
        except Exception as e:
            print(f'Error in {file}:', e)


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    menuBar = MacOSMenuBar()
    app.run()
