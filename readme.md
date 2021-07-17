# Toy Robot Simulator

This application simulates a toy robot on a **5x5** board. 

## About

There are 5 commands available:

	 - PLACE x, y, direction
	 - MOVE
	 - LEFT
	 - RIGHT
	 - RESET
Any commands outside of these 5 will be ignored. The robot will only be able to move or rotate when it has been placed.
Assumes coordinates (0,0) to be bottom left corner of the board while (4,4) is the top right corner.

## Deployment
This application is deployed continuously using github actions and AWS Elastic Beanstalk at http://test-environment2.eba-azxxntm3.ap-southeast-1.elasticbeanstalk.com/ with automated testing using python's unittest library.