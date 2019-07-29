import React from 'react'
import { Link } from 'react-router-dom'
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
                {year.facts.sort((a,b) => new Date(a.date_of_fact) - new Date(b.date_of_fact)).map(fact => (
                  <VerticalTimelineElement key={fact.id}
                    className="vertical-timeline-element"
                    date={<img className="fact-image" src={fact.image} />}
                    iconStyle={{ background: 'rgb(59, 67, 81)', color: '#fff' }}
                    icon=""
                  >
                    <Link to={`/facts/${fact.id}`}>
                      <h5 className="dates">{fact.date_of_fact}</h5>
                      <h5 className="location">{fact.location}</h5>
                      <h4 className="vertical-timeline-element-title">{fact.name}</h4>

                    </Link>
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
