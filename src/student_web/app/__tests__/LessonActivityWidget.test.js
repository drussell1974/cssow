import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonActivityWidget, LessonActivityWidgetItem } from '../widgets/LessonActivityWidget';


let lesson = 
    {
        "id": 220,
        "institute_id": 5,
        "department_id": 2,
        "title": "Types of CPU architecture",
        "order_of_delivery_id": 3,
        "course_id": 11,
        "scheme_of_work_name": "A-Level Computer Science",
        "topic_id": 1,
        "topic_name": "Algorithms",
        "parent_topic_id": 0,
        "parent_topic_name": "Computing",
        "related_topic_ids": "",
        "key_stage_id": 5,
        "key_stage_name": "",
        "year_id": 12,
        "year_name": "",
        "key_words": {
        "265": "Abstraction",
        "335": "3D printer"
        },
        "summary": "Von Neumann architecture and Harvard architecture\\; CISC and RISC",
        "pathway_objective_ids": [],
        "pathway_ks123_ids": [],
        "created": "2019-01-15T14:36:57",
        "created_by_id": 2,
        "created_by_name": " ",
        "published": 1,
        "orig_id": 0,
        "url": "/course/1277611/department/56/schemeofwork/11/lessons/220",
        "resources": [
            {
              "id": 117,
              "title": "A level: OCR Specification Order",
              "publisher": "Craig and Dave, YouTube, 2019",
              "page_note": "Dijkstras shortest path",
              "page_uri": "https://youtu.be/cm1Zcinds_w",
              "md_document_name": null,
              "type_id": null,
              "type_name": null,
              "type_icon": null,
              "lesson_id": 220,
              "course_id": 11,
              "last_accessed": "",
              "created": "2020-02-17T06:48:00",
              "created_by_id": 2,
              "created_by_name": " ",
              "published": 1,
              "is_expired": false
            },
            {
              "id": 118,
              "title": "Computerphile",
              "publisher": ", YouTube, 2019",
              "page_note": "Dijkstra\"s Algorithm",
              "page_uri": "https://youtu.be/GazC3A4OQTE",
              "md_document_name": null,
              "type_id": null,
              "type_name": null,
              "type_icon": null,
              "lesson_id": 220,
              "course_id": 11,
              "last_accessed": "",
              "created": "2020-02-17T06:48:00",
              "created_by_id": 2,
              "created_by_name": " ",
              "published": 1,
              "is_expired": false
            },
            {
              "id": 119,
              "title": "OCR AS and A Level Computer Science",
              "publisher": "PM Heathcote and RSU Heathcote, PG Online, 2016",
              "page_note": "The TCP/IP Protocol Stack - pages 122 - 123",
              "page_uri": "",
              "md_document_name": "The-TCP_IP-Protocol-Stack.md",
              "type_id": 10,
              "type_name": "Markdown",
              "type_icon": "fa-book",
              "lesson_id": 220,
              "course_id": 11,
              "last_accessed": "",
              "created": "2020-02-17T06:48:00",
              "created_by_id": 2,
              "created_by_name": " ",
              "published": 1,
              "is_expired": false
            }
          ]
    };

describe('LessonActivityWidget', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonActivityWidget />);
       
        expect(
            container.textContent
        ).toMatch("");
    })

    it('renders list of markdown resources', () => {
        render(<Router><LessonActivityWidget lesson={lesson} /></Router>);

        expect(
            container.querySelectorAll('ul.activities a.activity-link--markdown')
        ).toHaveLength(3);
    })

    describe('LessonActivityWidgetItem', () => {
        let render, container;
        
        beforeEach(() => {
            ({render, container} = createContainer());
        })
    
        it('renders empty model', () => {
            render(<LessonActivityWidgetItem />);
           
            expect(
                container.textContent
            ).toMatch("");
        })

        it('renders link text', () => {
            
            render(<Router><LessonActivityWidgetItem lesson={lesson} resource={lesson.resources[0]} /></Router>);

            expect(
                container.querySelector('li a.activity-link--markdown').textContent
            ).toMatch("A level: OCR Specification Order")
        })

        it('renders link href', () => {
            
            render(<Router><LessonActivityWidgetItem lesson={lesson} resource={lesson.resources[2]} /></Router>);

            expect(
                container.querySelector('li a.activity-link--markdown').getAttribute('href')
            ).toMatch("/lesson/220/activity/119/The-TCP_IP-Protocol-Stack.md")
        })
    })
})