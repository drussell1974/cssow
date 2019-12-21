import React, { Fragment } from 'react';

const GoogleAnalyticsWidget = ({trackingId}) => {
    if(trackingId === undefined || trackingId === ""){
        return (<Fragment></Fragment>);
    } else {
    let ga = {
        'Google Analytics':
            {
                trackingId:{trackingId}
            }
        };
        
        return (
            <script type="text/javascript">
                analytics.initialize(ga);
            </script>
        )
    }
};

export default GoogleAnalyticsWidget;