import React from 'react'
import axios from 'axios'
import { VerticalTimeline, VerticalTimelineElement }  from 'react-vertical-timeline-component'
import 'react-vertical-timeline-component/style.min.css'

class Home extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount() {
    axios.get('/api/years')
      .then(res => this.setState({ years: res.data}))
      .catch(err => console.log(err))
  }

  render() {
    if (!this.state.years) return null
    console.log(this.state.years)
    return (
      <section className="home-page">
        {this.state.years.map(year => (
          <div key={year.id} className="accordion">
            <input type="radio" id={`accordion-${year.id}`} name="accordion-radio" hidden />
            <label className="accordion-header" htmlFor={`accordion-${year.id}`}>
              {year.year}
            </label>
            <div className="accordion-body">
              <VerticalTimeline>
                {year.facts.map(fact => (
                  <VerticalTimelineElement key={fact.id}
                    className="vertical-timeline-element"
                    date={<img className="fact-image" src={fact.image} />}
                    iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
                    icon=""
                  >
                    <h4>{fact.date_of_fact}</h4>
                    <h3 className="vertical-timeline-element-title">{fact.name}</h3>
                    <p>{fact.bio}</p>
                  </VerticalTimelineElement>
                ))}
              </VerticalTimeline>
            </div>
          </div>
        ))}
      </section>
    )
  }
}

export default Home
