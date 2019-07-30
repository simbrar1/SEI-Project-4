import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import FactsForm from './FactsForm'

class NewFacts extends React.Component {
  constructor() {
    super()

    this.state = { data: {} }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    this.getYears()
  }

  getYears() {
    axios.get('/api/years')
      .then(res => {
        const years = res.data.map(year => year.year)
        this.setState({ years })
      })
      .catch(err => console.log(err))
  }

  handleChange({ target: { name, value}}) {
    const data = {...this.state.data, [name]: value}
    this.setState({ data }, () => console.log(this.state.data))
  }


  handleSubmit(e){
    e.preventDefault()

    axios.post('/api/facts', this.state.data,{
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.response.data))
  }

  render() {
    if (!this.state.years) return null
    return (
      <section className="section">
        <div className="card new-fact">
          <div className="create-new">
            <div className="container">
              <FactsForm
                data={this.state.data}
                years={this.state.years}
                submitText="Create"
                handleChange={this.handleChange}
                handleSubmit={this.handleSubmit}
              />
            </div>
          </div>
        </div>
      </section>
    )
  }

}

export default NewFacts
