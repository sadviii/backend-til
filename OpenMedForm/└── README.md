OpenMedForm, SNOMED CT & iSNOMED – Learning Notes

 OpenMedForm

OpenMedForm is a healthcare platform that helps convert clinical forms and documents into structured digital forms. I understood that instead of manually creating every field of a medical form, OpenMedForm can use AI to understand a form or PDF and generate a digital version of it. The forms are represented using structured formats such as JSON Schema, Data Schema, UI Schema and Print Schema. JSON Forms is used to render these forms, while Ajv can be used for validation. AI can also be used to create a form from a prompt and refine an existing form based on new instructions.

Technologies Used
 technologies such as React, Next.js and TypeScript for the frontend, and Node.js, NestJS and REST APIs for the backend. PostgreSQL is used as the database with Prisma as the ORM. It also involves JSON Forms, JSON Schema and Ajv for form creation and validation. For AI-based processing, it can work with LLMs and vision-capable LLMs, especially when understanding PDF layouts and forms. I also learned about Flutter for mobile form rendering, Docker for containerization, GitHub Actions for CI/CD and cloud deployment.

 SNOMED CT

SNOMED CT is a standardized clinical terminology used in healthcare. It is not an AI model or an application. It provides standardized clinical concepts along with descriptions, relationships, hierarchies and unique identifiers. The main purpose is to make clinical information consistent and understandable across different healthcare systems. For example, different people may use terms such as "heart attack" or "myocardial infarction" to describe the same clinical condition. SNOMED CT provides a standardized way to represent the clinical meaning.

OpenMedForm vs SNOMED CT

The main difference I understood is that OpenMedForm and SNOMED CT solve different problems. **OpenMedForm focuses on creating and capturing clinical information through structured digital forms**, while **SNOMED CT focuses on standardizing the clinical meaning of healthcare information**. They can work together, but they are not the same technology. OpenMedForm can collect structured clinical data, and standardized terminology such as SNOMED CT can be used to represent the clinical concepts in that data.

 iSNOMED

iSNOMED is an AI-based clinical coding and mapping solution. It can process clinical text, understand the clinical meaning in that text and map the information to standardized clinical terminology and codes such as SNOMED CT and ICD-10. For example, if a clinical note contains information about a patient's condition, iSNOMED can use AI to understand the information and identify the relevant standardized clinical concept or code.

 SNOMED CT vs iSNOMED

The main difference is that **SNOMED CT is the standardized clinical terminology itself, whereas iSNOMED is an AI-based tool that can understand clinical information and map it to standardized terminology and code**. In simple terms, SNOMED CT provides the standardized clinical concepts, while iSNOMED uses AI to find the appropriate concepts or codes from clinical text.

AI vs SNOMED CT

AI, including LLMs and NLP, is a technology used to process and understand information. SNOMED CT is a standardized clinical terminology used to represent healthcare concepts consistently. They can work together in a healthcare application. For example, AI can understand a doctor's clinical note and identify the patient's condition, and SNOMED CT can then provide the standardized clinical concept used to represent that condition.

Overall Understanding

My overall understanding is that **OpenMedForm, iSNOMED and SNOMED CT have different roles in healthcare**. OpenMedForm is mainly related to digital clinical forms and structured data capture. iSNOMED uses AI to understand clinical text and perform clinical coding or mapping. SNOMED CT provides the standardized terminology used to represent clinical meanings. Together, these technologies show how healthcare information can move from **unstructured documents or clinical text → AI processing → structured and standardized clinical information**.
