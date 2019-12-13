import React from 'react';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';

class Index extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            Lessons: [],
            hasError: false,
        }
    }

    componentDidMount() {
        //handleRefresh();
        
        fetch("http://127.0.0.1:8000/api/schemeofwork/11/lessons?format=json"   )
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                console.log(data);
                this.setState({
                    Lessons: data.lessons, 
                    hasError:false,
                });
            },  
            (error) => {
                this.setState({
                    Lessons: [],
                    hasError: true,
                });
            }
        )
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
        
        this.state = {
            hasError: true,
        }
      }
      
    render() {
        return (
            <React.Fragment>
                <section id="banner" data-video="images/banner">
                        <div className="inner">
                            <header>
                                <h1>Full Motion</h1>
                                <p>A responsive video gallery template with a functional lightbox<br />
                                designed by <a href="https://templated.co/">Templated</a> and released under the Creative Commons License.</p>
                            </header>
                            <a href="#main" className="more">Learn More</a>
                        </div>
                    </section>

                <div id="main">
                        <div className="inner">
                            <LessonBoxMenuWidget data={this.state.Lessons} />
                        </div>
                    </div>

                <footer id="footer">
                        <div className="inner">
                            <h2>Etiam veroeros lorem</h2>
                            <p>Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis. </p>

                            <ul className="icons">
                                <li><a href="#" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
                                <li><a href="#" className="icon fa-facebook"><span className="label">Facebook</span></a></li>
                                <li><a href="#" className="icon fa-instagram"><span className="label">Instagram</span></a></li>
                                <li><a href="#" className="icon fa-envelope"><span className="label">Email</span></a></li>
                            </ul>
                            <p className="copyright">&copy; Untitled. Design: <a href="https://templated.co">TEMPLATED</a>. Images: <a href="https://unsplash.com/">Unsplash</a>. Videos: <a href="http://coverr.co/">Coverr</a>.</p>
                        </div>
                    </footer>
                </React.Fragment>
        )
    }
};

export default Index;