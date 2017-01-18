#!/usr/bin/python
# coding: utf8


# http://python-gtk-3-tutorial.readthedocs.org/en/latest/introduction.html
# Widgets:
# http://pygtk.org/pygtk2reference/class-gtkwidget.html
# Tutorial for Widgets:
# http://zetcode.com/gui/pygtk/signals/
# Übersicht über Wigets:
# http://www.pygtk.org/pygtk2reference/
# Widget Einstellungen
# http://www.pygtk.org/pygtktutorial/ch-settingwidgetattributes.html

# Sämtliche Eigenschaften der Widgets hier zu finden:
#http://nullege.com/codes/search?cq=gtk.checkbutton

# To do
# in Datei speichern (ist wohl noch ne Fehlermeldung, wenn nicht .wav gewählt wird)
# speichern einfach als button, nicht als checkbox

import pygtk
pygtk.require('2.0')
import gtk
import subprocess
import sys
import re

def scale_set_default_values(scale):
	scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
	scale.set_digits(1)
	scale.set_value_pos(Gtk.POS_TOP)
	scale.set_draw_value(True)

class eSpeak_Fenster:

	def __init__(self):
		self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", lambda w: gtk.main_quit())
		self.window.set_title("Thorstens eSpeak-Interface")
		self.window.set_border_width(10)
		box1 = gtk.VBox(False,0) # Parameter: 1 - alles gleich groß in der box, 2 - Lücken
		# Buttons
		#--------------------------------------
		# on_button_datei
		#------------------------------------
		#Dateibox_START
		dateibox = gtk.HBox(False,0)
		box1.pack_start(dateibox,False,False,0)				
		#Dateibox_ENDE

		# Button Start_START
		button2 = gtk.Button("Start")
		button2.connect("clicked",self.on_button_start)
		dateibox.pack_start(button2,True,True,0)
		button2.show()
		# Button Start_ENDE

		#Button Speichern als Datei_START
		self.button_datei = gtk.Button("In Datei speichern")
		self.button_datei.connect("clicked",self.on_button_save)
		self.button_datei.show()
		dateibox.pack_start(self.button_datei,True,True,100)				
		#Button Speichern als Datei_ENDE
		#Sprache einstellen_ANFANG
		self.combo_sprache = gtk.combo_box_new_text()
		self.combo_sprache.append_text('deutsch')
		self.combo_sprache.append_text('englisch')
		self.combo_sprache.set_active(0)
		self.combo_sprache.show()
		dateibox.pack_start(self.combo_sprache,True,False,100)
		#Sprache einstellen_ENDE
		#--------------------------------------
		dateibox.show()
		#--------------------------------------
		separator = gtk.HSeparator()
		separator.set_size_request(400, 5)
		#-----------------------------------
		box1.pack_start(separator, False, True, 5)
		separator.show()
		#-----------------------------------
		box_textfeld = gtk.HBox(False,0)
		box1.pack_start(box_textfeld,False,False,0)

		#Textwidget in die Box box_textfeld------------------------------	
		self.entry_text=gtk.Entry()
		box_textfeld.pack_start(self.entry_text,False,False,0)
		self.entry_text.set_text("Hallo Welt")
		print self.entry_text.get_text() 		
		self.entry_text.set_usize(400, 20)
		# anzeigen der Box und des Textfeldes
		box_textfeld.show();self.entry_text.show()
		#------------------------------

 		#-----------------------------------
		separator = gtk.HSeparator()
		separator.set_size_request(400, 5)
		box1.pack_start(separator, False, True, 5)
		separator.show()
		#-----------------------------------

		# Regler Box
		box_regler = gtk.VBox(False,0) # Parameter: 1 - alles gleich groß in der box, 2 - Lücken
		box1.pack_start(box_regler,False,False,0)				
		# Einzelne Regler
		# Regler Lautstärke 
		# Label dazu
		label1 = gtk.Label("Lautstärke")
		box_regler.pack_start(label1,False,False,5)
		label1.show()
		default_amp = 10	
		adj_regler = gtk.Adjustment(default_amp, 0.0, 20, 1, 0, 0)	# siehe: http://www.pygtk.org/pygtk2tutorial/ch-Adjustments.html		
		self.regler1 = gtk.HScale(adjustment=adj_regler)  
		box_regler.pack_start(self.regler1,False,False,5)
		#regler1.connect("value-changed", self.value_changed("amp")
		self.regler1.show()
		#Regler2-----------------------
		adj_regler = gtk.Adjustment(50, 0, 99, 1, 0, 0)	# Regler Pitch
		label2 = gtk.Label("Pitcher")
		box_regler.pack_start(label2,False,False,5)
		label2.show()

		self.regler2 = gtk.HScale(adjustment=adj_regler)
		box_regler.pack_start(self.regler2,False,False,5)
		self.regler2.show()
		#Regler3-----------------------
		adj_regler = gtk.Adjustment(160, 80, 240, 1, 0, 0)	# Regler Pitch
		label3 = gtk.Label("Geschwindigkeit")
		box_regler.pack_start(label3,False,False,5)
		label3.show()

		self.regler3 = gtk.HScale(adjustment=adj_regler)
		box_regler.pack_start(self.regler3,False,False,5)
		self.regler3.show()
		#-----------------------

		#-----------------------
		box_regler.show()		
		#--------------------------------------
		#--------------------------------------
		separator = gtk.HSeparator()
		separator.set_size_request(400, 5)
		#-----------------------------------
		box1.pack_start(separator, False, True, 5)
		separator.show()
		#-----------------------------------

		# Quit_START
		quitbox = gtk.HBox(False,0)
		box1.pack_start(quitbox,False,False,0)				
		button = gtk.Button("Quit")
		button.connect("clicked",lambda w: gtk.main_quit())
		quitbox.pack_end(button,False,False,5)
		button.show()		
		quitbox.show()
		# Quit_ENDE
		#--------------------------------------
		self.window.add(box1)
		box1.show()
		self.window.show()
		
	def separatorr(self):
		self.separator = gtk.HSeparator()
		self.separator.set_size_request(400, 10)
		self.box1.pack_start(self.separator, False, True, 5)
		self.separator.show()

	def on_button_datei(self,widget):
		print "Datei gewählt"
	def on_button_start(self,widget):
		sprache = self.combo_sprache.get_active_text()
		Sprache_Dict = {"deutsch":"de","englisch":"en"}
		sprache = Sprache_Dict[sprache]
		say = self.entry_text.get_text() 		# Rückgabe des Textfeldes
		volume = str(self.regler1.get_value())
		pitch = str(self.regler2.get_value())
		speed = str(self.regler3.get_value())
		subprocess.call(["espeak","-v","de","-a",volume,"-p",pitch,"-s",speed,"-v",sprache,say])  # mit Parameter -v wird die Sprache übergeben
	def on_button_save(self,widget):
		say = self.entry_text.get_text() 		# Rückgabe des Textfeldes
		volume = str(self.regler1.get_value())
		pitch = str(self.regler2.get_value())
		speed = str(self.regler3.get_value())
		self.widget_pfad = gtk.FileChooserDialog("Dateiname wählen",None,gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK),None)
		self.widget_pfad.set_current_folder("~/Dokumente/Programmierung/Python/Voice")
		self.widget_pfad.show()
		self.datei_filter = gtk.FileFilter()
		self.datei_filter.set_name("wav-Dateien")
		self.widget_pfad.add_filter(self.datei_filter)
		response = self.widget_pfad.run()
		if response == gtk.RESPONSE_OK:
			self.Datei = self.widget_pfad.get_file();self.Datei = str(self.Datei);self.Datei = re.search(r"(/home.*wav)",self.Datei)
			if self.Datei == None:
				print "Die Dateiendung muss mit .wav enden"
			elif self.Datei is not None:
				self.Datei = self.Datei.group(0)
				subprocess.call(["espeak","-v","de","-a",volume,"-p",pitch,"-s",speed,"-v",sprache,"-w",self.Datei,say])  # mit Parameter -v wird die Sprache übergeben
				print "Datei gespeichert"				
		elif response == gtk.RESPONSE_CANCEL:
			print "Nichts gewählt"
		self.widget_pfad.destroy()

def main():
    gtk.main()
    return 0            

if __name__ == "__main__":
    espeak = eSpeak_Fenster()
    main()

