### Helper Instructions

Each example app is self-contained and can be deployed to a Cloud Foundry
instance with `$ cf push`.

The slides are available at https://speakerdeck.com/ihuston/pydata-london-2015-getting-started-with-cloud-foundry-for-data-science.

What participants need to do:

1. Register on http://run.pivotal.io
2. Download CF CLI from https://github.com/cloudfoundry/cli
3. Clone the tutorial repo from http://github.com/ihuston/python-cf-examples
OR download file at http://tinyurl.com/cf-pydata

### Getting Started

If you do not have an account on a Cloud Foundry installation you can
register for a free trial at Pivotal Web Services (PWS) http://run.pivotal.io.

Download the Cloud Foundry Command Line Interface from the CF management console
or the CF Github repo: https://github.com/cloudfoundry/cli.
This provides the `cf` command which you will use to interact with a CF installation.

Target the CF installation API with `cf api`. For example for PWS:

    $ cf api https://api.run.pivotal.io

### Pushing your first app

The first app is in the folder `01-simple-python-app`.
Have a look at the code and then deploy using `cf push`.

You can inspect the app's streaming logs using `cf logs myapp`.

You can scale your app by changing the number of instances and the available RAM:

    $ cf scale myapp -i 5
    $ cf scale myapp -m 256M

### Pushing an app with PyData dependencies

The second app is in the folder `02-pydata-spyre-app`.
This app is built using [Spyre](https://github.com/adamhajari/spyre) by Adam Hajari.

This application uses a new feature of the official [Python buildpack](https://github.com/cloudfoundry/python-buildpack/)
to provision dependencies using `conda`.

The `environment.yml` file contains the `conda` environment specification.
The buildpack detects this file and uses `conda` instead of `pip` to install the dependencies.

Push the app using `cf push` and visit the app URL to see a simple interactive visualisation.

### Using data services

The third app is in the folder `03-services-redis`.

Services provide persistent storage and other useful resources for your applications.

First, create a free Redis service provided by Rediscloud:

    $ cf create-service rediscloud 30mb myredis

You can bind this to your apps making it available via the `VCAP_SERVICES`
environmental variable.

    $ cf bind-service myapp myredis

Look at the environmental variables your app has with `cf env myapp`.

Now you can push the third app which uses Redis as its backing store.

The manifest specifies that this app should be bound to the myredis service instance that you just created.

### Putting it all together

The fourth app is in the folder `04-learning-api`.

We can put everything we've learned into practice by building our own simple
machine learning API.

**Don't forget to stop all your apps when you are finished.**
