---
Minimal django project in support of [django ticket 24506](https://code.djangoproject.com/ticket/24506).
---

This repository contains two django projects using different django versions and is a working example that the django ticket 24506 has been fixed in django 1.8.

1. `Proxyuser17` uses django 1.7 which breaks when migrating as per ticket 24506.
2. `Proxyuser18` uses django 1.8 using the same models and it doesn't break.