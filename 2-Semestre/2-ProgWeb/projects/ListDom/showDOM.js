directChildren = Array.from(document.documentElement.children);
childTags = directChildren.map(child => child.tagName.toLowerCase());
childTags;

directChildren = Array.from(directChildren[1].children);
directChildren
childTags = directChildren.map(child => child.tagName.toLowerCase());
childTags;

directChildren = Array.from(directChildren[0].children);
childTags = directChildren.map(child => child.tagName.toLowerCase());
childTags;

const iterateChildren = (element) => {
    element = Array.from(element.children);

    element.forEach(child => {
        console.log(child);
    });
};

