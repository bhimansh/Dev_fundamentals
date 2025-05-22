### Prerequisites
- go version v1.23.0+
- docker version 17.03+.
- kubectl version v1.11.3+.
- Access to a Kubernetes v1.11.3+ cluster.


### Step1
**Initializes a new module in the current directory**  
```go mod init cars.com/cars-practice-kube```  
Defines your project as a module, so Go can track and manage dependencies.
Enables dependency management using Go modules (instead of GOPATH-based workflows).
Sets the module path, which is used as the import path for your code and sub-packages.
Marks the root of your Go project, allowing go build, go test, etc., to work correctly


### Step2
**Initializes a new kubernetes API project**  
```kubebuilder init --domain=cars.com```  
Kubebuilder is a framework for building Kubernetes APIs using custom resource definitions (CRDs) in Go. The **"init"** command will sets up a boilerplate project to develop the CRDs/Controllers in GO. The **"--domain"** option will customise and sets a suffix for the CRDs group. The boilerplate project will have contents similar to this:-  
"[ cars-practice-kube]$ ls  
cmd  config  Dockerfile  go.mod  go.sum  hack  Makefile  PROJECT  README.md  test".  
**NOTE:** YOU STILL NEED TO CREATE A API USING **"create api"** COMMAND TO HAVE CRD/CONTROLLER TEMPELATE CODE.


### Step3
**Create a new API (CRD/CONTROLLER)**  
```kubebuilder create api --group apps --version v1 --kind Cars```  
This command creates a new api under "apps" group of version "v1" and kind "Cars". Also, tempelate code files for the crd and controller(reconciller) will be generated, which will be updated by us to generate the desired behaviour of our CRDs and respective Controller.  
**The Directory Structure after this:**  
├── api/  
│   └── v1/  
│       ├── cars_types.go        # Schema definition  
│       └── groupversion_info.go  
├── internal/controllers/  
│   └── cars_controller.go       # Reconcile logic (empty scaffold)  
├── config/  
│   ├── crd/bases/               # CRD YAML  
│   └── samples/                 # Sample CustomResource YAML


### Step4
**Implement the code changes**  
In this step we will give our Cars CRD and it's respective Controller behavioural logic.
1. CRDs Defination: This is done using the "struct" present in the "<>_types.go" file.
    "Spec":- Desired State "User defined by User"
    "Status:- Observed State "Set by controller"
2. Controller Defination: This is the Implemented reconcilliation logic in "<>_controller.go" file. 


### Step5
**Generate the updated YAMLs and RBAC roles**  
```make maifests```    
**Purpose:** Generates Kubernetes CRD YAML manifests and RBAC roles.  
**What it uses:** controller-gen and kustomize.  
**What it affects:**
    Populates/updates:
        config/crd/bases/
        config/rbac/


### Step6
**Generate the GO code with latest API defination**  
```make generate```  
**Purpose:** Generates Go code (deepcopy methods, CRD types, etc.) from your API definitions.  
**What it uses:** controller-gen tool.  
**What it affects:**
    Updates zz_generated.deepcopy.go files.
    Regenerates scheme, groupversion_info.go, etc.


### Step7
**Build and Deploy the Docker image to deploy the Controller on the Kubernetes cluster**  
```IMG=<registory>/controller:latest make docker-build docker-push```  
```IMG=<registory>/controller:latest make deploy```

### Step8
**Create the instance of created CRD in kubernetes cluster using yaml**  
```kubectl apply -f cars-pratice-kube/samples/test.yaml```
