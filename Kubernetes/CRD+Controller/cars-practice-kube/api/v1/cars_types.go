/*
Copyright 2025.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package v1

import (
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// EDIT THIS FILE!  THIS IS SCAFFOLDING FOR YOU TO OWN!
// NOTE: json tags are required.  Any new fields you add must have json tags for the fields to be serialized.

// CarsSpec defines the desired state of Car's Engine.
type CarsSpec struct {
	// INSERT ADDITIONAL SPEC FIELDS - desired state of cluster
	// Important: Run "make" to regenerate code after modifying this file

	// start field represents the state of Car's Engine.
	// +kubebuilder:validation:Required
	// +kubebuilder:validation:Enum=ON;OFF
	Start string `json:"start,omitempty"`
}

// CarsStatus defines the observed state of Car's Engine.
type CarsStatus struct {
	// INSERT ADDITIONAL STATUS FIELD - define observed state of cluster
	// Important: Run "make" to regenerate code after modifying this file
	EngineStatus string `json:"engine_status,omitempty"`
}

// +kubebuilder:object:root=true
// +kubebuilder:subresource:status

// Cars is the Schema for the cars API.
type Cars struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`

	Spec   CarsSpec   `json:"spec,omitempty"`
	Status CarsStatus `json:"status,omitempty"`
}

// +kubebuilder:object:root=true

// CarsList contains a list of Cars.
type CarsList struct {
	metav1.TypeMeta `json:",inline"`
	metav1.ListMeta `json:"metadata,omitempty"`
	Items           []Cars `json:"items"`
}

func init() {
	SchemeBuilder.Register(&Cars{}, &CarsList{})
}
