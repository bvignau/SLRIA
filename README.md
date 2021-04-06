# SLRIA
Systematic Literrature Review assisted with IA

# HOW TO USE

* Create an empty directory to host your SLR and cd in
* Run ``slria --init `` to create a result folder, and an empty conf file
* Run ``slria --request `` to create a folder for each request with their meta.conf file
* Add all the paper selected with the request, fill the meta.conf file for each paper (provide title and year)
* fill the configuration document
* Run ``slria --start`` to merges all the papers, deletes duplicates paper and generate statistics for the 1st round
* Run ``slria --extract`` to extract all the references from all the papers in their corresponding folders
* Check all the files. It may have some issues in the extract process due to the PDF format. In general errors happend at the 1st and the last citation (missing or extra text)
* Run ``slria --merge`` to merges all the references and produces statistics for the snowball
* Dowload all the selected papers in the round2 folder
* Repeat extraction, check, merge etc until the end of your SLR
