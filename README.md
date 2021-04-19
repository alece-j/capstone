# **An Analysis of the Pali Canon**

#### By: Alec Edgecliffe-Johnson
---
### **Introduction**

The Pali Canon is the foundational collection of texts of the Theravada Buddhist Religion. It contains the oldest known records of the Buddha's teachings, compiled in written form about 500 years after the Buddha's death and maintained orally in the interim.

The Canon is a diverse collection of works that documents teachings, stories, exclamations, quotes and poetry grouped into 5 separate collections by later compilers. Although it is little known and little studied in the west, the Canon and commentaries on it, form the core of the religion for hundreds of millions of Theravada Buddhists, particularly in South East Asia.

Although translations from Pali (an ancient Sanskritic language) have existed for over one hundred years, the translations were often made by scholars who were not steeped in the living Buddhist monastic culture and discipline and often by those who did not practice. As such, it is unclear how often early translators had experiential insight into the meaning of often complex phenomena and concepts that are represented in the Canon. These insights are undoubtedly important for accurately representing a dead language (that contains many words/concepts with no direct equivalent in english) and, in turn, for outlining a path of practice to an unconditioned happiness that is as alive today as it was in the time of the Buddha.

In recent years, however, as a result of an enormous effort by several English-speaking Buddhist monks, a large portion of the Pali Canon has been translated and made available online. The suttas that are the data for this project come from www.dhammatalks.org which hosts suttas translated by Ajahn Geoff, a monk of nearly 45 years in the Kammathana (Thai Forest Tradition) lineage. He has significant experience in translating both from Pali and Thai and is an inspiring monk in conduct and learnedness.

---
### **Problem Statement**

The purpose of this project is two-fold:
1. To do significant, public-facing, Natural Language Processing analysis on the Pali Canon. This allows me to develop a Tableau dashboard for each sutta and Nikaya (collection) that outlines time to read, recommendations for further exploration from the author and wordclouds to try to capture themes through words.

  An investigation like this, at this scale, has, to my knowledge, never been conducted before. Given the recency of the availability of strong English translations of the Canon coupled with  fairly recent advances in Machine Learning algorithms that will be employed, the absence of an existing analyis at this level is less surprising than it might initially appear. Furthermore, the cross-section of lay-Theravadan Buddhists (non-monks) who are dedicated to reading the original texts (not 'Dhamma' books by other lay-Buddhist 'Dhamma teachers'), and people with an understanding of the tools needed to do this analysis probably yields quite a small number of people.

2. To develop a recommendation algorithm for suttas that could be used to support the development of particular mental qualities, themes and understandings within the religion. One could consider this to be a sort of 'Netflix' for information on how to develop along a path to an unconditioned happiness. For a rough understanding of the functionality, one can imagine a scenario where a user would input a sutta on a particular theme they were interested in learning more about or developing further and receive back five suttas that share content similarity.

---
## **Executive Summary**

After extensive review, EDA, preprocessing and several 'dead-ends' with modeling, Google's pretrained Bidirectional Encoder Representations from Transformers (BERT) model was employed to develop a recommendation engine that produced results with extremely high cosine similarities (.95 or higher for top results in most cases) and low euclidean distances. This model was then used to develop a Flask app that takes user input in the form of a sutta reference (eg. 'MN 1' for 'Majjhima Nikaya 1') and delivers five suttas out of the entirety of this translated portion of the canon (1306 suttas in total) with the highest cosine similarity score.

The data for the project was scraped with Octoparse over 30 separate scrapes from dhammatalks.org. The suttas were then cleaned extensively, removing notes, see also comments, navigation and introductory commments from the body of the text itself. The suttas were then merged into 13 different dataframesone for each of the four 'stand-alone' compilations; seven additional dataframes for each of the seven sub-collections of the fifth compilation (Khuddaka Nikaya); one for the entirety of the Khuddaka Nikaya; lastly, one for all five compilations.

Prior to EDA or modeling the suttas were preprocessed to remove punctuation, lowercase the words, remove stop words and tokenize the text. In the EDA phase, word counts were collected that informed total and average read times for each sutta and collection (based on 265wpm rates), and page length (based on 250 words per page). This information was then used to create sutta by sutta [visualizations](https://public.tableau.com/profile/alec.johnson2268#!/vizhome/SuttaInformation/SuttaView) as well as full collection [visualizations](https://public.tableau.com/profile/alec.johnson2268#!/vizhome/FullSuttaVizualizations/ThePaliCanon) in Tableau.


In the modeling phase, in addition to the BERT production model, other similarity modeling approaches included the use of TFIDF vectorizations with dot product and euclidean distances as well as Doc2Vec document embeddings with cosine similarity and euclidean distance measures. The BERT model outperformed on both similarity and difference measures.

In addition to the similarity models, three topic analysis models were also developed. The first which employed TFIDF with TruncatedSVD produced topic word clusters that, while interesting, were not suitable for later use in a user interface. The second and third topic analysis models were both Latent Dirichlet Allocation (LDA), one on tokenized word alone and one on tokenized words with TFIDF applied. These both had coherence scores of about .49 and, again, the topic clusters were not relevant to the development of a front end application.

Finally, a Flask app was developed in order to give users the ability to interact with the BERT model with an attractive front end. In this version of the model, the ability to select number of results and type of similarity measure (euclidean distance v. cosine similarity) was not included. Instead a standard five results with cosine similarity was selected for all queries, however, users can input a reference of any one of the 1306 translated suttas on dhammatalks.org as they see fit.

---
## **Conclusions and Next Steps**

This project took, as its starting point, the relative non-linearity of the Pali Canon as a challenge to build a way to navigate the suttas. This was accomplished in two ways. Firstly, I built robust visualizations that allow users to get a sense of how individual suttas and collections interact with eachother and to allow for an entry point into the suttas with this information. Secondly, I developed a Flask application that generates content recommendations for 'next reads' for any sutta with a BERT model in the background and very high cosine similarity scores.

Moving forward I would like to do the following:
1. Refine Flask application
2. Further tune BERT model
3. Extend model to include Audio2Vec on Dhamma dhammatalks
