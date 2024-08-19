#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const tar = [];

  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      tar.push(list[i]);
    }
  }
  return tar.length;
};
