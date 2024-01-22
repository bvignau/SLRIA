# SLRIA
Systematic Literrature Review assisted with IA

# Install

run the following commands : 

```bash
chmod +x install.sh
chmod +x main.py

./install.sh
pip install -r requirements.txt
```

If you want to install it globally and have a cli you can use the following commands : 

```bash
sudo mkdir /usr/bin/slria
sudo cp *.py /usr/bin/slria/
sudo cp empty.conf /usr/bin/slria
echo 'alias slria="python /usr/bin/slria/main.py"' >> ~/.zshrc
```

# HOW TO USE

* Create an empty directory to host your SLR and cd in
* Run ``slria init ./SLRIA_TUTO`` to create a folder called SLRIA_TUTO. This folder will contains one config faile SLR.conf and two folders : csv and final bib. 
Fill the SLR.conf file. Add all the requests that will be made to each search engine. Provide one request per ligne such as : 

```yaml
[Request]
r0 = "Personal Identification with PPG"
r1 = "Personal recognition with PPG"
r2 = "Signature with PPG"
r3 = "biometric identification with photoplethysmography"
r4 = "Personal Identification with photoplethysmography"
```
Then provide the value for the actual round, the number of paper you want per request and a name for each database. If you use the same database multiples times with differents times laps, it recommended to add the time laps at the end of the names.

```yaml
[SLRIA]
round = 1
papers_by_request = 10
databases = scholar_17_20,scholar,pubmed,pubmed_17_20,web_of_science,web_of_science_17_20
```

The Filter section help to filter and classify the papers. It also help to merge duplicate references.
To merge the references, we use a comparison score with a threshold. For each references, we extracted a maximum of fields. But due to differences in references format, sometimes fields are missings. This is why we made a matching algorithm based on all the fields. We give 40 points if the title is the same, and 10 pts per identical authors and 1 point for all other fields.  To match the titles between two references, we use the damerau-levenshtein distance with a score below to 5. We add this flexibility to be resilient to the invisible characters and errors due to reference extract.

This values can be easly modified in the file reference.py.

To merge duplicate references, we compare all the references two by two and compute the comparison score. If the score is higher than the one given in the filter section, the two references are merged. Be carreful, this system is not perfect and requier a manual check.

The kwords are used to determine the level of interest of a paper. The number of keywords in the title determine the level of interest in the paper, so give a maximum of words in this section. Moreover, the nkwords fields allow to automatically drop all the papers where the title which contains less key wordsthan this value.

```yaml
[Filter]
comparison = 35
appearance = 
kwords = "biometric,identification,signal,personal,body,healthcare,photoplethysmographic,diagnostic,interindividual,qrs,authentication,physiological,signature,recognition,authentication,analysis,study,PPG,representation,photoplethysmography,identity,study,identifier,verification,novel"
nkwords = 1
```

* Run ``slria request ./`` to create a folder for each request with their meta.conf file
* Add all the paper selected with the request, fill the meta.conf file for each paper (provide title, authors and year)
* Run ``slria start ./`` to merges all the papers, deletes duplicates paper and generate statistics for the 1st round
* Run ``slria extract ./`` to extract all the references from all the papers in their corresponding folders
* Check all the files. It may have some issues in the extract process due to the PDF format. In general errors happend at the 1st and the last citation (missing or extra text)
* Run ``slria merge ./`` to merges all the references and produces statistics for the snowball
* Dowload all the selected papers in the round2 folder and change the round number in the config file.
* Repeat extraction, check, merge etc until the end of your SLR
