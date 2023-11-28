oc policy add-role-to-user \
   edit \
   system:serviceaccount:openshift-gitops:openshift-gitops-argocd-application-controller \
   --rolebinding-name=argocd-edit \
   -n object-detection
   
oc policy add-role-to-user \
   edit \
   system:serviceaccount:openshift-gitops:openshift-gitops-argocd-application-controller \
   --rolebinding-name=argocd-edit \
   -n redhat-ods-applications
