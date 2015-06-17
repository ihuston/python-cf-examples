# Simple Cloud Foundry based machine learning API

Modified from code originally written by Alexander Kagoshima
See the full version at https://github.com/alexkago/ds-cfpylearning

This app demonstrates a very simple API that can be used to create model instances, feed data to them and let these models retrain periodically. Currently, it uses redis to store model instances, model state and data as well - for scalability and distributed processing of data this should be replaced by a distributed data storage.

For all the examples below replace ```http://<model_domain>``` with your Cloud Foundry app domain.


Create a model
--

```
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "model_type": "LinearRegression", "retrain_counter": 10}' http://<model_domain>/createModel
```


Add in some data
--

This example shows how to send data into the model created before, s.t. the linear regression model becomes y = x. Since we set the retrain_counter to 10 previously, the model will retrain after it received the 10th data instance.

```
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 1, "label": 1}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 2, "label": 2}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 3, "label": 3}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 4, "label": 4}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 5, "label": 5}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 6, "label": 6}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 7, "label": 7}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 8, "label": 8}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 9, "label": 9}' http://<model_domain>/ingest
curl -i -X POST -H "Content-Type: application/json" -d '{"model_name": "model1", "input": 10, "label": 10}' http://<model_domain>/ingest
```


Look at all created models
--

There's a very rudimentary view on the redis set of all models that have been created:

```
http://<model_domain>/models/
```


Look at model details
--

This lets you check out the status of the previously created model as well as its trained parameters:

```
http://<model_domain>/models/model1
```

License
--

This application is released under the Modified BSD license. Please see the LICENSE.txt file for details.
