Feature: Test the login functionality

Scenario: Login Icon presence
	Given: I launch chrome browser
	When: I open the homepage
	Then: I verify if the login icon is present and I click on it

Scenario: Wrong Input
	Given: I locate the input fields and see if they are present
	When: I enter the wrong credentials 
	And: Click the login button
	Then: I check if I am logged in, assert error should be present

Scenario: Correct Input
	Given: I locate the input fields and see if they are present
	When: I enter the correct credentials
	And: click the login button
	Then: I check if Iam logged in, test should pass


{\rtf1}