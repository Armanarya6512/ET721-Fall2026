Arman Arya
Professor Wu
Software Development Practicum
November 15, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

* What was the initial test coverage? The starter project had 11 tests and 53% code coverage. The model code was at 60% and the API routes were only at 46%.
* What is the final test coverage you were able to achieve? I reached 100% coverage for both app/models.py and app/routes.py.
* How many tests did you end up having? I ended up with 49 tests: 19 API tests, 8 model tests, 11 search and model-helper tests, and 11 expiration date tests.

## Untested Code: Effects

* Were you able to understand all features and different use cases of the code without the tests? Not completely. I could see the basic endpoints, but I could not tell how the app should behave in edge cases, such as updating an id that does not exist or averaging an empty list, until I read the code closely and wrote tests for those cases.
* What did you think of having to test the API manually? It was slow and easy to get wrong. Running the server and opening URLs in a browser only checks one thing at a time, and I would have to repeat all of it after every change.
* What was the result of having few tests on your understanding of the API? With few tests I only had a partial picture of the API. Each new test I wrote made the expected behavior of a route or function clearer, so the tests became a kind of documentation.

## Adding Tests

* How did you go about adding more tests to the code? I ran the coverage report to see which lines were not tested, then wrote tests for those lines one group at a time: the four empty unit tests first, then the search function, then the update, delete, search and home routes. After each group I re-ran coverage to confirm the number went up.
* What is the difference between a unit test and an API test? Do they bring different values? A unit test checks one small piece of code by itself, such as the average quantity function or the name validation. An API test sends a real HTTP request, such as PUT or DELETE, and checks the status code and the response, so it verifies that the routes, the database and the models work together. Unit tests find problems quickly and show exactly where they are, while API tests show that the whole feature works the way a user would use it. Both are valuable.

## Automation

* What were the benefits of automating test coverage? Running one command (coverage run -m pytest) runs every test and shows exactly which lines are still untested, which is much faster than checking by hand. With continuous integration, such as GitHub Actions, the same tests would run automatically on every push or pull request, so broken code would be caught before it reaches customers.

## New Features

* What was your experience like having to add new features when you tested baseline code? After the baseline code was fully tested, I added the suggested features: an expiration date on each fruit, an endpoint that returns expired fruit (/api/fruits/expired), and an analytics endpoint (/api/fruits/analytics) that returns the total number of fruits, total quantity, average quantity, and most common fruit. I wrote 20 new tests for them. Because the existing tests were already in place, I could run the full suite after each change and confirm that nothing that worked before had broken.
* Did it give you any feeling of security when trying out new features? Yes. With 100% coverage and all tests passing, I feel much more confident making changes, because a failing test would point out the problem right away.

## Future

* What do you hope to takeaway from the experience having to write tests? I want to make testing a regular habit instead of something I do at the end. In future projects I plan to write tests as I build each feature, check coverage often, set up automated testing with GitHub Actions, and add tests for more unusual inputs, such as missing fields in a POST request, so the API is protected against more kinds of failures.

