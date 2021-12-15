# Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP

## Introduction
Understanding patients' demand on medication products and their perceptions about the products performance and related services are important for pharmaceutical industries to succeed in the competitive market. Most research on medication products analysis is based on consumers’ purchase history and drug reviews, the regular analysis on product reviews are mainly focused on sentiment analysis about the positive and negative comments. However, the more specific attributes about the performance of the drugs, for example “effectiveness”, needs to be explored and there are lots of details about patients’ needs that cannot be discovered by this approach.     
In this study, I retrieved the drug reviews and related information from WebMD, a widely used website about medication, and built a prediction system to uncover the performance of drugs from patients reviews by natural language processing models and investigated the patients’ needs by text-mining.

## Data Resource
The main data will be collected form [WebMD drugs reviews](https://www.webmd.com/drugs/2/index) by web scraping. The drug reviews include the drug review text, four numerical variables, ”Effectiveness”, ”Easy to Use”, ”Satisfaction” in the scale of 1 to 5 and number of votes for “helpfulness” (the score starts from 0). It also includes the date of posting, the related information about the patients and the patients’ conditions. [Click here for the python codes of web scraping](https://github.com/sarahzhao21/Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP/blob/730e8065213ab42669476047511c440df4cc30e0/wd_review_webscraping.py).

## Methods
1. Data collection by web scraping, the data come from the [WebMD website] (https://www.webmd.com/), I used “cfscrape” and “bs4” packages and collected more than 70 thousand instances.
2. Data clean and organizing, the original review text contains lots of noise and null values, which has been removed, then a dataframe with 14 columns has been created (include “date”, “condition”, “effect’, “ease”, “satisfy” and “helpful” etc).   
3. Prepare for the word embedding. Convert the the reviews into tokens list or bigrams list by nltk.tokenize and (BigramAssocMeasures BigramCollocationFinder). 
4. Build the prediction system by different algorithms include: Naive Bayes, Keras and LSTM.  
5. Text-mining to explore the most important phrases or terms that make the review impacting. Topic modeling has been implemented by Latent Dirichlet Allocation (by gensim library).
6. Another prediction system has been built based on the features created by topics. The algorithms for machine learning include: Naive Bayes, Random Forest and SVC.
[Please click here for details and python codes](https://github.com/sarahzhao21/Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP/blob/730e8065213ab42669476047511c440df4cc30e0/SI630%20Project_xinyiz.ipynb). 

![Accuracy and Loss by 'keras' deep learning algorithm](https://github.com/sarahzhao21/Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP/blob/3132a559d929e3d4a26fad79821bacfee5582b9d/Picture1.png)

![Topic Modeling](https://github.com/sarahzhao21/Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP/blob/3132a559d929e3d4a26fad79821bacfee5582b9d/topic.png)

## Conclusion
By this study, I retrieved the patients’ drug reviews and related information from WebMD and used the “effectiveness”, “ease-to-use”, “satisfaction” and “helpfulness” ground truth labels to implement deep learning on the review text. The evaluation metrics indicate that this system is accurate to make the precision on “effectiveness”, “ease-to-use” and “satisfaction”. In the meantime, we used topic modeling to investigate the core elements from the review text and extract ten major topics, which reveals the most critical issues about people's health situation, for example body weight, sleep time, chronic pain and heart disease.  This kind of study would be beneficial to the pharmaceutical industry on market forecast and new products design.    
[My Blog](https://xinyiz-13686.medium.com/discover-customers-health-care-demand-drug-review-analysis-by-natural-language-processing-8aaa5c9f2e57)    
[Please click here for details](https://github.com/sarahzhao21/Discover-Patients-Health-Care-Demand----Drug-Review-Analysis-by-NLP/blob/3132a559d929e3d4a26fad79821bacfee5582b9d/SI630%20Final%20Project%20Report_xinyiz.pdf)
