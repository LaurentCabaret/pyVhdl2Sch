clean:
	rm *.pdf &
	rm *.png &
	rm *.ps &
	rm *.svg &
	rm tb_*.vhd &
	find . -name "*.pyc" -exec rm -rf {} \; &

check:
	sh pep8Checker/check.sh
