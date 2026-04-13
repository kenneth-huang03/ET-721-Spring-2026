Kenneth Huang 
Huixin Wu
ET 721 D2
April 8th, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

* What was the initial test coverage? 
* What is the final test coverage you were able to achieve? 
* How many tests did you end up having?

## Untested Code: Effects

* Were you able to understand all features and different use cases of the code without the tests?
* What did you think of having to test the API manually? 
* What was the result of having few tests on your understanding of the API?

## Adding Tests

* How did you go about adding more tests to the code?
* What is the difference between a unit test and an API test? Do they bring different values?

## Automation

* What were the benefits of automating test coverage?


Initially the only test coverage was about 50%. After completing the assignment, we should
have covered the remaining 50%. The total in the file we worked on was 8 tests. Most of the
code was understandable even before the tests were made for it, but the manual tests against
the API allowed us to make sure what we are intending is what happens. The amount of tests
there are doesn't correlate to how well I can understand the program. Having tests just allows
me to know that what I expect of the program is what the program produces. The API tests(not
in this repository) allow us to test that the public facing application is behaving as expected
while the unit tests allow us to test that the internal logic is behaving as expected. Benefit
of using this hand made but automated testing makes it so that if we have any change to any
part of the program, the tests can see what breaks, and if it had any effect on anything
else without having to manually sift through the entire project one file at a time.
