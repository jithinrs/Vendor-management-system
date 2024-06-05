SETUP

> Create a virtual environment by using the command python -m venv venv
> Activate the virtual environment
    windows: venv/Scripts/activate 
    ubunutu : source venv/bin/activate
> cd to vendor_management_system folder and run the command "pip install -r requirements.txt"
> Run the project using the command python manage.py runserver

VENDOR RELATED ENDPOINTS

# Create a new vendor
Endpoint: vendorManagement/vendors/
method: POST
payload : {
    "name" : "Nithin RS",
    "contact_details": "vendors contact details",
    "address": "vendors address"
}

#Get all vendors
Endpoint: vendorManagement/vendors
method : GET

#Get a specific vendor
Endpoint: vendorManagement/vendors/id/
method : GET

#update a specific vendor
Endpoint: vendorManagement/vendors/id/
method : PUT
payload:{
    {
    "name" : "Nithin RS",
    "contact_details": "updated contact details",
    "address": "updated address"
}
}

#delete a vendor details
Endpoint: vendorManagement/vendors/id/
method: DELETE


PURCHASE ORDER RELATED ENDPOINTS

#create a new purchase ORDER
Endpoint:vendorManagement/purchase_orders/
method:POST
payload: {
    "items" : {
        "pencil" : "some details"
    },
    "quantity" : 12444,
    "vendor" : 2,
    "delivery_date" : "2024-06-15T08:29:17.394285Z",
    "issue_date" : "2024-06-04T08:03:17.872556Z"
}

#Get a purchase order data
Endpoint:vendorManagement/purchase_orders/id/
method:GET

#Get list of all purchase order data
Endpoint: vendorManagement/purchase_orders/
method: GET

#update a purchase order data
Endpoint : vendorManagement/purchase_orders/id/
method : POST
payload: {
    "items" : {
        "pencil" : "some details"
    },
    "quantity" : 12444,
    "vendor" : 2,
    "status" : "completed",
    "quality_rating" : 5,
    "delivery_date" : "2024-06-15T08:29:17.394285Z",
    "issue_date" : "2024-06-04T08:03:17.872556Z"
}

#delete a purchase order data
Endpoint : vendorManagement/purchase_orders/id/
method : DELETE




#Get the vendor performance data
Endpoint: vendorManagement/vendors/2/performance
method: GET


#Acknowledge the purchase order
Endpoint : vendorManagement/purchase_orders/<order_id>/acknowledge
method:PUT
payload: None