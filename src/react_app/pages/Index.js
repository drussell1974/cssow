import React from 'react';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';

class Index extends React.Component {
    render() {
        let lessons = [{
            id:1,
            title: "Curabitur id purus feugiat, porttitor.",
            summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
            image_url: "images/pic01.jpg",
            url: "https://youtu.be/s6zR2T9vn2a",
        },{
            id:2,
            title: "Sed a ante placerat, porta.",
            summary: "Nullam quis malesuada mauris. Vivamus vitae augue eget quam porta pretium nec in ligula. Aenean ullamcorper leo at mi hendrerit.",
            image_url: "images/pic02.jpg",
            url: "https://youtu.be/s6zR2T9vn2b",
        },{
            id:3,
            title: "Nullam bibendum hendrerit dolor, in.",
            summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
            image_url: "images/pic03.jpg",
            url: "https://youtu.be/s6zR2T9vn2c",
        },{
            id:4,
            title: "Donec pellentesque sit amet lorem",
            summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
            image_url: "images/pic04.jpg",
            url: "https://youtu.be/s6zR2T9vn2d",
        },{
            id:5,
            title: "Nullam a ultrices mi. Suspendisse",
            summary: "Nam at malesuada mi. Cras non consectetur sapien. Etiam eget justo egestas, sagittis mauris a, luctus quam. Quisque vitae sapien.",
            image_url: "images/pic05.jpg",
            url: "https://youtu.be/s6zR2T9vn2e",
        },{
            id:6,
            title: "Donec sit amet felis id",
            summary: "Integer feugiat eget libero eu eleifend. Pellentesque molestie pellentesque urna non malesuada. Mauris blandit accumsan est, at aliquam mauris tempus.",
            image_url: "images/pic06.jpg",
            url: "https://youtu.be/s6zR2T9vn2f",
        }];

        return (
            <React.Fragment>
                <section id="banner" data-video="images/banner">
                        <div class="inner">
                            <header>
                                <h1>Full Motion</h1>
                                <p>A responsive video gallery template with a functional lightbox<br />
                                designed by <a href="https://templated.co/">Templated</a> and released under the Creative Commons License.</p>
                            </header>
                            <a href="#main" class="more">Learn More</a>
                        </div>
                    </section>

                <div id="main">
                        <div class="inner">
                            <LessonBoxMenuWidget data={lessons} />
                        </div>
                    </div>

                <footer id="footer">
                        <div class="inner">
                            <h2>Etiam veroeros lorem</h2>
                            <p>Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis. </p>

                            <ul class="icons">
                                <li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
                                <li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
                                <li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
                                <li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
                            </ul>
                            <p class="copyright">&copy; Untitled. Design: <a href="https://templated.co">TEMPLATED</a>. Images: <a href="https://unsplash.com/">Unsplash</a>. Videos: <a href="http://coverr.co/">Coverr</a>.</p>
                        </div>
                    </footer>
                </React.Fragment>
        )
    }
};

export default Index;