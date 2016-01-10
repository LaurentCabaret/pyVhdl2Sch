test: gui.py test.py
	python test.py

gui.py: gui.ui
		pyuic4 gui.ui > gui.py
