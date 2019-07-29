import React from 'react'
import axios from 'axios'
import FactsForm from './FactsForm'
import Auth from '../../lib/Auth'

class FactsEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: {} }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/facts/${this.props.match.params.id}`)
      .then(res => {
        const data = res.data
        data.year_number = res.data.year.year
        this.setState({ data }, () => this.getYears())
      })
      .catch(err => console.log(err.response))
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
    const data = this.state.data
    delete data.year
    axios.put(`/api/facts/${this.props.match.params.id}`, data,{
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.props.history.push(`/facts/${this.props.match.params.id}`))
      .catch(err => console.log(err.response))
  }


  render() {
    if (!this.state.years) return null
    console.log(this.state)
    return(
      <section className="section">
        <div className="main">
          <FactsForm
            data={this.state.data}
            years={this.state.years}
            submitText="Update"
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
          />
        </div>
      </section>
    )
  }
}


export default FactsEdit
