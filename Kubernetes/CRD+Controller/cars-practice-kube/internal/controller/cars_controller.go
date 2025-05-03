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

package controller

import (
	"context"
	"fmt"
	"time"

	"k8s.io/apimachinery/pkg/runtime"
	ctrl "sigs.k8s.io/controller-runtime"
	"sigs.k8s.io/controller-runtime/pkg/client"
	logf "sigs.k8s.io/controller-runtime/pkg/log"

	appsv1 "rajat.com/cars-practice-kube/api/v1"
)

// CarsReconciler reconciles a Cars object
type CarsReconciler struct {
	client.Client
	Scheme *runtime.Scheme
}

// +kubebuilder:rbac:groups=apps.rajat.com,resources=cars,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=apps.rajat.com,resources=cars/status,verbs=get;update;patch
// +kubebuilder:rbac:groups=apps.rajat.com,resources=cars/finalizers,verbs=update

// Reconcile is part of the main kubernetes reconciliation loop which aims to
// move the current state of the cluster closer to the desired state.
// TODO(user): Modify the Reconcile function to compare the state specified by
// the Cars object against the actual cluster state, and then
// perform operations to make the cluster state reflect the state specified by
// the user.
//
// For more details, check Reconcile and its Result here:
// - https://pkg.go.dev/sigs.k8s.io/controller-runtime@v0.20.4/pkg/reconcile
func (r *CarsReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
	_ = logf.FromContext(ctx)

	// TODO(user): your logic here
	var in appsv1.Cars
	if err := r.Get(ctx, req.NamespacedName, &in); err != nil {
		return ctrl.Result{}, err
	}

	if in.Spec.Start == "ON" {
		time.Sleep(10 * time.Second)
		fmt.Println("Car Engine is ON, Stopping engine after 10sec")
		time.Sleep(10 * time.Second)
		in.Spec.Start = "OFF"
	} else {
		time.Sleep(10 * time.Second)
		fmt.Println("Car Engine is OFF, Starting engine after 10sec")
		time.Sleep(10 * time.Second)
		in.Spec.Start = "ON"
	}
	in.Status.EngineStatus = in.Spec.Start

	// Update status on the etcd
	if err := r.Status().Update(ctx, &in); err != nil {
		return ctrl.Result{}, err
	}

	// Update spec
	if err := r.Update(ctx, &in); err != nil {
		return ctrl.Result{}, err
	}
	return ctrl.Result{}, nil
}

// SetupWithManager sets up the controller with the Manager.
func (r *CarsReconciler) SetupWithManager(mgr ctrl.Manager) error {
	return ctrl.NewControllerManagedBy(mgr).
		For(&appsv1.Cars{}).
		Named("cars").
		Complete(r)
}
