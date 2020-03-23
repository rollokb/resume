# Rollo Konig-Brock - Resume

Passionate about programming, simplicity and pragmatism. Primarily a
Python developer, with a focus on writing high performing applications.

Also skilled in the frontend, and DevOps, and smatterings of C++ when needed.

## Experience

### Contract - Lead Python Developer - IHS Markit Datalake Team
*London - March 2019 - Present*

Bought in as a replacement for a departing team of contractors, I
refactored and rearchitected a large part of IHS Markit's Datalake
project. Playing a key part in transitioning a proof of concept, to a
product sold to major institutions.

In the initial months I was responsible for refactoring the core service
into a maintainable, serviceable API; while also onboarding a remote team of
former Java developers. The refactor required a rework of the database
layer, Elasticsearch, and the core Flask Application; without causing
breaking changes to internal business lines using the Datalake.

I used this as an opportunity to train the group of new developers on
SQLAlchemy, Flask, and Python. Through the introduction of SQLAlchemy, we
were able to refactor deeply nested complex SQL views, into simple model based
representations, dramatically improving performance.

I was also responsible for integrating the authentication layer within the
wider company, introducing SAML and AWS IAM Role based authentication; and
transitioning to an API gateway design. This allowed me to remove large
amounts of superfluous infrastructure dedicated to authentication, reducing
attack surface. The understanding of the infrastrucutrea gained through this
enabled me to refactor signifant portions of Kuberentes config, and Terraform
(with the help of DevOps).

More recently I helped in finding a new London team to help develop a
service which would provide an interface major data science tools, including
Spark, Pandas, KNIME, Athena, and more. A major focus of this project was high
performance streaming, which I utilised Parquet and Arrow heavily for. In
order to achieve memory efficient streams, I had to write Cython and C++
patches for Apache Arrow.


### Contract - Python Developer - Barclays
*London - September 2018 - Feburary 2019*

For Barclays’ penetration testing team within the Chief Security Office we were
tasked with developing an ad-hoc internal tool into a service deployable within
Barclays’ corporate network. The tool was turned into a product which would call
a Kubernetes API to run manage and scale short lived deployments of various
security software packages and analyse the results.

As part of a rewrite, my aim was to bring the project in line with best
practices. I upgraded the project from Python 2 to 3; introduced unittests
(via PyTest); and made the codebase PEP8 compliant. Structual changes included
replacing adhoc low level solutions to data-storage, caching and messaging,
with MongoEngine, and Flask-Cache (as a wrapper around Redis).

New features included a RESTful API; a tree based versioning system for
inputs; single sign on; a new UI built with JavaScript and BootStrap; and
comprehensive audit logging and history of user actions.

### Contract - Python Developer - MCSaatchi/UK Department of International Trade
*London - April 2018 - July 2018*

For the UK's Department of International Trade's 'Invest in Great' campaign I
created a small application to deliver a personalised investment report for
companies interested in moving to the UK. The core of this project was a PDF
generator that would return professional quality documents. Built around this:
was a Django CMS for creation and moderation of content; and a separate service
for the frontend communicating over a HTTP API.

The PDF generator was written using WeasyPrint, which is a Python library for
the conversion of HTML to PDF documents. This posed some fun challenges using
CSS to create flowing documents, and an opportunity to use some of CSS's lesser
known print media features. Other technologies used included Celery,
Cloudfoundy, Hawk Authentication, and various government specific APIs.

This project is publicly available in the following repositories:

 * <https://github.com/uktrade/invest-pir-api>
 * <https://github.com/uktrade/invest-pir-ui>
 * <https://github.com/uktrade/invest-pir-api-client>

And can be viewed here:

 * <https://www.great.gov.uk/international/invest/perfectfit/>

### Contract - Full Stack Developer - TicTrac/Sport Relief
*London - November 2017 - March 2018*

Hired by TicTrac to develop a complex digital campaign for Sport Relief to be
delivered on a tight 2 month deadline. Tasked with adapting a complex Django
API; I delivered new large amounts of functionality and worked with the, iOS,
Andriod, and Angular.JS teams, to foster an understanding of new features in a project
that often had changing requirements.

Due to personnel issues, at times I was asked to fill in for the Angular.JS team,
implementing new functionality, directives and SCSS. I used this as an
opportunity to give the iOS and Andriod teams a working example of designs and
API implementation.

Shortly before launch, I worked on scaling the app, focusing on SQL optimisation,
achieving 100x performance increases in key areas. After launch I continued to
provide support to the application as it's userbase grew from nothing to over 250k.
I also provided on-site support for Sport Relief during Sport Relief week.

### Python Developer - ComplyAdvantage
*London - January 2017 - September 2017*

As a Python developer, I worked on the design and development of distributed
and fault tolerant microservices, while also building carefully designed APIs.
Due to the size of the datasets used at ComplyAdvantage I payed careful attention
to performance and achieved a number of notable performance gains.

While at ComplyAdvantage I lead the development of a new JSON-API compliant
REST API, that unified two separate APIs, while paying careful attention to
permissions granularity and performance. I also refactored existing code, such
as moving a Tornado API to Flask and, optimising and replacing raw SQL with
SQLAlchemy.

I also had a customer facing role where I was responsible for the import,
export and migration of customer data. To handle the increasing volume I wrote
set of tools that leveraged Pandas, Numpy, S3, SQS and Lambda, which enabled
the customer success team to take over the much of the process.

### Contract - Full Stack Developer, Lystable (Now KaloHQ)
*London - June 2016 - December 2016*

With Lystable, I have primarily been a back end developer with a focus on
improving infrastructure of the backend, as well as the features that which
requires full stack development. I worked on features such as:a
webhook framework; audit logging systems; notification behaviors; database
analytics; as well as third party integrations.

The primary technologies used were, Python, Postgres, ElasticSearch, RabbitMQ,
and a messaging framework built on top of rabbit called Nameko. I introduced
the use of Postgres' asynchronous `NOTIFY` capability log changes to the
database in a fault tolerant and scalable manner. I have also worked
on creating a location aware search, leveraging OpenStreet Maps and
ElasticSearch.

While my primary role at Lystable was the backend, I also worked on React.JS
applications adding smaller features like integrations to third party services,
and updates to how the application consumes our API.

### Contract - Full Stack Developer, Bought By Many
*November 2015 - June 2016*

As a full stack developer for Bought By Many I worked in agile teams on
consumer facing Django websites such as ExoticDirect.com and BoughtByMany.com;
Flask based micro-services; and frontend SaaS applications.

I worked on everything from simple front end components written in CoffeeScript
and SASS, to more complex realtime websocket powered user-interfaces. While work
on Bought By Many’s Python based microservices involved adding new features, such
as: new endpoints; analytical Mongo aggregations; and API integrations with third
parties and our own services, to several large Flask applications.

I created a new frontend SaaS application to replace the one written in
Backbone.JS. This application served as a frontend to Bought By Many’s micro
services; which needed a tool to visualize data and administrate aspects of the
business. I rewrote the app in modern ES6; using RxJS (a functional JS library)
as the primary library, while using D3.js for data visualisations. The build
depended on PostCSS and Babel, and jQuery Globalize for
internationalization (I18N).

### Full Stack Developer, Seven Stones - Total Health
*January 2015 - October 2015*

As a full stack web developer for Seven Stones Total Health, I worked on data
driven static sites, used to market pharmaceuticals, and iOS applications which
ranged from maintaining e-Details (interactive displays targeted for trade fairs
and conferences) to internal projects which were part of the company’s wider
strategy.

Maintenance of the e-Details involved iterating existing Ember.js Cordova
applications to work on later iOS platforms. I was also tasked with building an
internal iOS project which relied heavily on presentation and video, a technical
challenge I faced was the requirement that HLS video steams be available
offline, which I successfully solved using Apple’s Swift to implement an
intelligent proxy cache embedded in the app. New projects were done with a
combination of native languages and React Native.

I also worked on building responsive static sites based on look-and-feel
designs, with responsive data visualisations using D3.js.

### Contract - Web Developer, KS Agency London
*October 2014 - January 2015*

Worked for KS Agency implementing designs and ideas from the designers. This
mostly involved implementing designs from Photoshop, and effectively
communicating the sites' behaviour.

I created clean and responsive websites with semantic HTML, and clean
preprocessed CSS, which degraded gracefully in older browsers. I also created a
number of simple web applications within Drupal (PHP) for advanced searching of
content and data.

While I was there, I expanded the tool chain by introducing Git, SASS and Amazon
Web Services, allowing for smoother deployment.

### iOS Developer, Business & Finance Magazine (Dublin)
*December 2012 - May 2013*

As a freelancer I designed and built an iOS app for Business & Magazine (and
accompanying CMS) for readers to read their monthly magazine (before everything
went responsive).

I worked to communicate with people at Business & Magazine to maintain their
visual style on mobile; and to implement as their request a, ‘pay per issue
system’.

For this I created a CMS for the app written in Django with a basic
administration interface, which provided an API for the delivery content, and
registration of in app purchases which were used to drive the pay per issue
system.

### Intern, Canonical Ltd.
*February 2011 - March 2011*
As an intern at Canonical I worked on the Ubiquity Desktop Installer, which
is the graphical installer used on the Ubuntu series of operating systems.

The desktop installer when I began was primarily written in Python 2, under
guidance I helped port some of the installer to Python 3.

The installer also needed a style update (in line with the rest of the OS). I
was introduced to the ‘QT’ framework which uses CSS for styling the UI; I was
responsible for updating some of the UI under the guidance of a graphic
designer.

### GitHub Profile

[https://github.com/rollokb](http://bit.ly/2hpfKv0)

### Skills (Basically buzzwords)

This is basically to aid recruiters searching for technologies, which I'm
skilled with but have not explicitly mentioned.

* Python/Django/Flask
* C++/CMake
* Pandas/Numpy/Arrow
* JIRA
* JavaScript/ES6
* Obj-C/Swift
* Docker
* RabbitMQ/AMPQ/SQS
* Amazon AWS/IAM
* UNIX/Linux/OSX
* Design Experience designing with Photoshop, Illustrator and Indesign.

### Contact

rollokb+recruitment@gmail.com

I am happy to take calls, but due to volume I prefer an introductory email.
