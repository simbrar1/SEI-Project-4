import React from 'react'

const Comment = ({ content, id, user, handleCommentDelete, isCommentOwner }) => (
  <div >
    <div className="1">{content}</div>
    {isCommentOwner(user) && <button
      className="btn btn-sm"
      onClick={() => handleCommentDelete(id)}
    >
      Delete Comment
    </button>}
  </div>
)

export default Comment
