import React, { Fragment }from 'react';

export const LessonActivityWidget = ({data}) => {
    //if(data === undefined) {
    //    return <React.Fragment></React.Fragment>;
    //} else {
        return (
            <Fragment>
                <div class="markdown-body">
                    <h1>A list of first steps to carry out:</h1>
                    <ul>
                            <li>Lorum ipsum dolor</li>
                            <li>Lorum ipsum dolor</li>
                            <li>Lorum ipsum dolor</li>
                            <li>Lorum ipsum dolor</li>
                    </ul>
                    
                        <h2>Lorem ipsum dolor sit amet</h2>
                        <p>dconsectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio, adipisci quas excepturi maxime quae totam ducimus consectetur?</p>
                    <p>This is a procedure. It carries out a task by printing <em>"Hello, World!"</em>.</p>
                    <code>
                        def a_procedure():
                    &nbsp;&nbsp;&nbsp;&nbsp;print "Hello, World!"
                    </code>
                    <p>This is a function. It returns something. This functions returns the string <em>"Hello, World!</em>, then prints it outside the function.</p>
                    <code>
                    def a_function():
                    return "Hello, World!"
                    print a_function()
                    </code>
                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius praesentium recusandae illo eaque architecto error, repellendus iusto reprehenderit, doloribus, minus sunt. Numquam at quae voluptatum in officia voluptas voluptatibus, minus!</p>
                    <pre>
                    client yarn build
                    </pre>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut consequuntur magnam, excepturi aliquid ex itaque esse est vero natus quae optio aperiam soluta voluptatibus corporis atque iste neque sit tempora!</p>
               </div>                
            </Fragment>
        );
    //}
}