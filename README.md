# Talent Bridge API

## Objective

The Talent Bridge API powers a job board application designed to connect recruiters and job seekers. It provides a RESTful backend with endpoints for managing job postings, applications, and applicant workflows.

---

## Key Features

* **Authentication & Profiles**
  - Role-based authentication for recruiters and applicants
  - Profile management for both recruiters and applicants (e.g., company profiles for recruiters, personal profiles for applicants)

* **For Recruiters**
  - Create and manage job listings.
  - View applications and applicant profiles
  - Accept or reject job applications

* **For Applicants**
  - Browse and apply for job opportunities
  - Track and manage submitted applications

---

## Tech Stack

* **Django:** A high-level Python web framework used for building the RESTful API. It provides built-in tools for authentication, routing, database interaction, and security.

* **Django REST Framework:** An extension of Django that simplifies the process of building, testing, and documenting RESTful APIs. It enables easy handling of serialization, permissions, authentication, and API versioning.

* **PostgreSQL:** A powerful, open-source relational database system used to store structured data such as users, properties, bookings, and reviews. It offers strong data integrity, advanced querying, and scalability.

---

## Documentation

Comprehensive API documentation is available at: /api/docs