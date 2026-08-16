# Agent Skills Catalog

This catalog defines optional skills that Conductor may recommend. Every source
is pinned to an immutable Git revision. The installer must use the repository,
revision, and path together and must validate the downloaded frontmatter before
enabling a skill.

**Party semantics**: `1p` means the repository is controlled by the named
publisher's public organization; it does not mean Conductor has audited the
skill or established that it is safe. `3p` means a community publisher.

## Firebase Skills

### firebase-ai-logic-basics

- **Description**: Integrate Firebase AI Logic into web applications.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-ai-logic-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase`, `AI Logic`, `Gemini API`, `GenAI`

### firebase-app-hosting-basics

- **Description**: Deploy and manage web apps with Firebase App Hosting.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-app-hosting-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase App Hosting`, `Next.js`, `Angular`

### firebase-auth-basics

- **Description**: Set up and use Firebase Authentication securely.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-auth-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase Authentication`, `Auth`, `Sign-in`

### firebase-basics

- **Description**: Set up Firebase and add it to an application.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase`, `Setup`

### firebase-data-connect

- **Description**: Build Firebase Data Connect backends with PostgreSQL.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-data-connect-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase Data Connect`, `PostgreSQL`, `GraphQL`

### firebase-firestore

- **Description**: Set up Firestore, security rules, and SDK usage.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-firestore/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firestore`, `Database`, `Security Rules`

### firebase-hosting-basics

- **Description**: Deploy static web apps with Firebase Hosting.
- **Repository**: firebase/agent-skills
- **Publisher**: Firebase
- **Revision**: `073edf7bb747c27b9c911a9126adaa5bc4648fdc`
- **Path**: `skills/firebase-hosting-basics/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `firebase`, `firebase-admin`
  - **Keywords**: `Firebase Hosting`, `Static Hosting`

## DevOps Skills

### google-cicd-deploy

- **Description**: Deploy applications to Google Cloud services.
- **Repository**: gemini-cli-extensions/devops
- **Publisher**: Gemini CLI Extensions
- **Revision**: `85812c656ac5e04349e93958b2f2823e15c5adf5`
- **Path**: `skills/google-cicd-deploy/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `gcloud`
  - **Keywords**: `Cloud Run`, `GCS`, `GKE`, `Deployment`, `Google Cloud`

### google-cicd-pipeline-design

- **Description**: Design and implement CI/CD pipelines on Google Cloud.
- **Repository**: gemini-cli-extensions/devops
- **Publisher**: Gemini CLI Extensions
- **Revision**: `85812c656ac5e04349e93958b2f2823e15c5adf5`
- **Path**: `skills/google-cicd-pipeline-design/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Keywords**: `CI/CD`, `Pipeline Design`, `Google Cloud`, `Architecture`

### google-cicd-release-orchestration

- **Description**: Orchestrate Google Cloud releases and delivery pipelines.
- **Repository**: gemini-cli-extensions/devops
- **Publisher**: Gemini CLI Extensions
- **Revision**: `85812c656ac5e04349e93958b2f2823e15c5adf5`
- **Path**: `skills/google-cicd-release-orchestration/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `skaffold`
  - **Keywords**: `Cloud Deploy`, `delivery pipeline`, `skaffold.yaml`,
    `clouddeploy.yaml`

### google-cicd-terraform

- **Description**: Provision Google Cloud infrastructure with Terraform.
- **Repository**: gemini-cli-extensions/devops
- **Publisher**: Gemini CLI Extensions
- **Revision**: `85812c656ac5e04349e93958b2f2823e15c5adf5`
- **Path**: `skills/google-cicd-terraform/SKILL.md`
- **Party**: 1p
- **Detection Signals**:
  - **Dependencies**: `terraform`
  - **Keywords**: `Terraform`, `GCP`, `GCS Backend`, `Infrastructure as Code`
