#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completedTasksByUser = {};
    const tasks = JSON.parse(body);
    
    for (const task of tasks) {
      if (task.completed === true) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    }
    
    console.log(completedTasksByUser);
  } else {
    console.error('An error occurred. Status code:', response.statusCode);
  }
});
