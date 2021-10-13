# AI Email Writer Program

#### Brief Overview
Email writing with GPTJ

## Install for Linux/Python 3
#### Installation
```
$ git clone https://gitlab.com/stackaccount1/ira_email_writer.git

cd into the location

/ira_email_writer$ pip3 install .

```

#### Dependencies
Should download above, if not download requirements via requirements.txt in repository


## Update the .txt spreadsheet with your emails 
/src/ira_email_writer/data -> librebook.txt 
update the file with your own emails, do not touch the question and answer row, keep the same formatting, save, and close 


## Import the package into your python project, and run the email write function
### A few Examples

```
import ira_email_writer as iew

iew.emailwriterv2("Email from someone here")

```
The functions returns an email response

```
import ira_email_writer as iew

iew.emailwriterv2("hey")

```
The functions returns: hey, how are you today?

```
import ira_email_writer as iew

iew.emailwriterv2("Will you get me TPS reports by Friday?")

```
The functions returns: Sorry boss, will have to wait till Monday
