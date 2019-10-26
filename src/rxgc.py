from pywinauto.application import Application

app = Application(backend="uia").start("RPG_Maker_MV_Extended_Generator.exe")
dlg = app['RPG Maker MV Extended Generator']
try:
  print(dlg.Menu.File)
  dlg.Menu.MenuItem3.dump_tree()
# dlg.minimize()
# dlg.menu_select()
# print(dlg.print_control_identifiers())
# dlg.MenuStrip1.print_control_identifiers()
# dlg.print_control_identifiers()
# print(dlg.MenuItem3.menu_item())
# dlg.MenuItem3.child_window()
# dlg.wait(10)
# try:
  # dlg.Menu.File.print_control_identifiers()
finally:
  dlg.close()

# dlg.menu_select("File")

