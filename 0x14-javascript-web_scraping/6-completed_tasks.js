#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    console.log('Number of completed tasks by user:');
    Object.keys(completedTasksByUser).forEach(userId => {
      console.log(`User ID ${userId}: ${completedTasksByUser[userId]}`);
    });
  } catch (err) {
    console.error('Error parsing JSON data:', err);
  }
});
