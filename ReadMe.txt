README: Predicting Hospital Readmission Risk Using MIMIC-III Dataset with LLM and RAG

This repository contains all coding documentation and implementation instructions for evaluations, future reference, and potential employment opportunities.

Included Files:

* /README.txt 				→ Project documentation and instructions
* /CNN.ipynb 				→ Convolutional Neural Network implementation used to classify patient data patterns and augment structured features.
* /data\_preprocessing.ipynb 		→ Complete data cleaning and preprocessing pipeline, including missing value handling, z-score normalization, one-hot encoding, and preparation of severity indices (OASIS, SIRS, qSOFA, APS III, mLODS).
* /LLM.ipynb 				→ Large Language Model integration pipeline, embedding discharge summaries using ClinicalBERT, retrieving top-k similar cases with FAISS, and generating contextual prompts processed through Mistral-7B using local Ollama deployment.
* /ML\_modelling\_withICU.ipynb 	→ Machine learning models (Logistic Regression, XGBoost, LightGBM, SVM) trained on structured data including ICU-specific variables.
* /ML\_modelling\_withoutICU.ipynb 	→ Machine learning models excluding ICU-specific variables for comparative performance analysis.

Implementation Instructions:

1. Clone the repository.
   git clone <repository-url>
   cd <repository-folder>

2. Install Required Libraries:
   pip install -r requirements.txt
   (Core packages: pandas, numpy, scikit-learn, tensorflow, keras, transformers, faiss-cpu, langchain, pinecone-client, streamlit)

3. Prepare Data:

   * Obtain MIMIC-III dataset with appropriate access.
   * Run data\_preprocessing.ipynb to clean and format both structured and unstructured data.

4. Run Embedding & Retrieval:

   * Use LLM.ipynb to generate ClinicalBERT embeddings and build FAISS indices.
   * Integrate RAG framework to retrieve similar patient narratives and fuse them with structured risk scores.

5. Train Models:

   * Open ML\_modelling\_withICU.ipynb and ML\_modelling\_withoutICU.ipynb.
   * Follow the notebook steps to train, tune, and evaluate models using accuracy, AUC-ROC, and F1-score.
   * Apply grid search and cross-validation for hyperparameter tuning.

6. Deep Learning Layer:

   * Explore CNN.ipynb for convolutional model setup focused on sequential/temporal patterns.

7. Deployment:

   * Deploy interactive Streamlit app for real-time predictions, SHAP explainability plots, and natural language outputs.
   * For privacy-preserving LLM inference, use Ollama for local deployment of Mistral-7B.

Evaluation Highlights:

* Best performance achieved with LightGBM: 73% accuracy, 0.79 AUC-ROC, 0.76 weighted F1.
* Ablation studies confirm that including LLM-derived contextual features improves prediction metrics by 6–11% over structured-only models.
* SHAP interpretability identifies key features (hospital expiration flags, ICU stay length, SOFA scores, admission age).

Future Directions:

* Expand testing to multi-hospital datasets.
* Optimize semantic retrieval strategies.
* Introduce human-in-the-loop feedback for refining LLM prompt quality.
* Explore multi-modal data integration (imaging, time-series signals).
* Prepare publication materials for submission to conferences or journals.

Poster & User Interface Demo - https://drive.google.com/drive/u/0/mobile/folders/1IJyPbQsFxuHHa-ah0a6V9nllzCFD70YE?usp=drive_link

Personal Email

Haswanth Valluru		- 	haswanth0007@gmail.com
Venkata Vidhya Sagar Keerthi 	- 	master.sagar248@gmail.com
Parul Rathore 			- 	parulrathore2110@gmail.com
Sruthi Srikanth			- 	sruthii.srikanth@gmail.com
Vatsal Bhalani 			- 	vat03bhalani@gmail.com
Maneesh Choppara 		- 	maneesh_choppara@outlook.com

LinkedIn Profiles

Haswanth Valluru		- 	https://www.linkedin.com/in/haswanth-valluru/
Venkata Vidhya Sagar Keerthi 	- 	https://www.linkedin.com/in/venkata-vidhya-sagar/
Parul Rathore 			- 	https://www.linkedin.com/in/parulrathore/
Sruthi Srikanth			- 	https://www.linkedin.com/in/srikanth-sruthi/
Vatsal Bhalani 			- 	https://www.linkedin.com/in/vatsal-bhalani/
Maneesh Choppara 		- 	http://linkedin.com/in/maneesh-choppara-3833b2183/