build:
	cd src && go build -o ../bin/contactlist && cd ..

clean:
#	Check if .git directory exists to ensure that this is done in the root of the repository
	if [ -d ".git" ] || [ -d "bin" ]; then rm -r bin; fi

run:
	bin/contactlist