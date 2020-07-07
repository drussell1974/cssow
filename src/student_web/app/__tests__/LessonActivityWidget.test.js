import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonActivityWidget } from '../widgets/LessonActivityWidget';

let lesson = 
    {
        "id": 220,
        "title": "Types of CPU architecture",
        "order_of_delivery_id": 3,
        "scheme_of_work_id": 11,
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
        "url": "/schemeofwork/11/lessons/220",
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
              "scheme_of_work_id": 11,
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
              "scheme_of_work_id": 11,
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
              "md_document_name": "",
              "type_id": 6,
              "type_name": "Book",
              "type_icon": "fa-book",
              "lesson_id": 220,
              "scheme_of_work_id": 11,
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

    it('renders empty markdown_html an empty string', () => {
        render(<LessonActivityWidget data={lesson} markdown_html={""} />);

        expect(
            container.textContent
        ).toMatch("");
    })

    it('renders heading2', () => {
        render(<LessonActivityWidget data={lesson} markdown_html={"<h1>Markdown content</h1><p>Lorem ipsum dolor sit amet.</p>"} />);

        expect(
            container.querySelector('h2').textContent 
        ).toMatch("Activity");
    })

    it('renders markdown-body with markdown_html', () => {
        render(<LessonActivityWidget data={lesson} markdown_html={"<h1>Markdown content</h1><p>Lorem ipsum dolor sit amet.</p>"} />);
    
        expect(
            container.querySelector('section.markdown-body').textContent 
        ).toMatch("Markdown contentLorem ipsum dolor sit amet.");
    })
})