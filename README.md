# hard-hats
Hard Hants Wanted

## Installation

```
touch .env
```

> Make sure to fill `.env` with correct contents (see [`.env.example`](/.env.example)).

## Decisions

This document will contain design, architecture, and other major project decisions made along the way for reference to whoever takes up the project.

## Requirements / Product Priorities

- Simple
- Cheap
- Functional

Our goal is to to achieve these basic requirements while still creating an architecture that is extensible beyond an MVP.
We will use *Django*, which will allow us to initially build a simplified full stack web application that serves out static web pages initially. If the project grows in scope, Django's flexibility will allow us to convert it into a REST API Framework that can exclusively become the backend, if we need to have dynamic frontend pages using React or another frontend library.
We plan on cheaply hosting this on AWS EC2 or a lightweight server.

## Order of Tackling Deliverables

- Design pages (already done)
- Create backend schema for the database
- Build out the backend
- Create a barebones frontend to hook into backend
- Add styling/functionality to frontend as needed
- Once it's working locally, host on a server
