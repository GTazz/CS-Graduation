directChildren = Array.from(document.children);
console.log(directChildren);
childTags = directChildren.map(child => child.tagName);
console.log(childTags);


directChildren = Array.from(directChildren[0].children);
console.log(directChildren);
childTags = directChildren.map(child => child.tagName);
console.log(childTags);


const iterateChildren = (element) => {
    element = Array.from(element.children);

    element.forEach(child => {
        console.log(child);
    });

};
