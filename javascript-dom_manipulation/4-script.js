const my_list = document.querySelector('ul.my_list');
const new_item = document.querySelector('#add_item');

new_item.addEventListener('click', function(){
    const list = document.createElement('li');
    const item = document.createTextNode('Item');
    list.appendChild(item);
    my_list.appendChild(list);
})