Hello!

The reason there are a ton of notebooks is because we were running different models on different machines at the same time, since the training and hyperparameter tuning took so long.
The titles for the notebooks denote what they specifically were for; the content in them is pretty similar, the main differences across the files is the max token length;
We ran tuning for different token lengths at the same time, to ensure we had several models to draw from. The metrics of all the models we ran can be found in metrics.xlsx
Another file of note is basic-analysis, which perfomed, well, basic analysis for us to understand the data and make some graphs to put in the report. 

Sorry this repo looks so messy, but most of the notebook files contain similar code, so not super worth look at each one, unless you wanna see the model output straight from the source instead of the spreadsheet. 
